import logging
from typing import List, Dict, Optional
from service_discovery import ServiceDiscovery

logger = logging.getLogger(__name__)

class ServiceCatalogue:
    """Manages the catalogue of premium services available to businesses."""
    
    def __init__(self):
        self.catalogue = []
        
    def update_catalogue(self) -> None:
        """
        Updates the service catalogue by fetching from all providers.
        
        Logs the number of services added and any errors encountered.
        """
        logger.info("Starting service catalogue update.")
        discovery = ServiceDiscovery()
        services = discovery.discover_services()
        self.catalogue.extend(services)
        logger.info(f"Catalogue updated with {len(services)} new services.")

    def add_service(self, service: Dict) -> None:
        """
        Adds a single service to the catalogue.
        
        Args:
            service: Dictionary containing service details.
        """
        if not self._is_valid(service):
            logger.error("Invalid service data. Service not added.")
            return
        self.catalogue.append(service)
        logger.info(f"Service {service['name']} added to catalogue.")

    def _is_valid(self, service: Dict) -> bool:
        """Validates service data."""
        required_fields = ['name', 'provider', 'features']
        return all(field in service for field in required_fields)

    @property
    def services(self) -> List[Dict]:
        """Returns the current list of services in the catalogue."""
        return self.catalogue.copy()