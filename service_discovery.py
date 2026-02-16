import logging
from typing import List, Dict, Optional
import requests

logger = logging.getLogger(__name__)

class ServiceDiscovery:
    """Handles discovery of available services from external providers."""
    
    def __init__(self):
        self.service_providers = ['provider1', 'provider2']
        
    def discover_services(self) -> List[Dict]:
        """
        Discovers and returns a list of available premium services.
        
        Returns:
            List of service details including name, provider, and features.
            
        Raises:
            Exception: If unable to fetch services from any provider.
        """
        services = []
        for provider in self.service_providers:
            try:
                response = requests.get(f'https://{provider}/services')
                if response.status_code == 200:
                    services.extend(response.json())
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch services from {provider}: {str(e)}")
        
        if not services:
            logger.warning("No services discovered across all providers.")
            
        return services

    def _fetch_provider_catalogue(self, provider: str) -> Optional[List[Dict]]:
        """
        Fetches service catalogue from a specific provider.
        
        Args:
            provider: Name of the provider to fetch services from.
            
        Returns:
            List of services or None if failure.
        """
        try:
            response = requests.get(f'https://{provider}/catalogue')
            if response.status_code == 200:
                return response.json()
            logger.error(f"Provider {provider} returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed to provider {provider}: {str(e)}")
        return None