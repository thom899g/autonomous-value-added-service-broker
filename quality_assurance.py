import logging
from typing import Dict, Optional
from service_catalogue import ServiceCatalogue

logger = logging.getLogger(__name__)

class QualityAssurance:
    """Evaluates and ensures the quality of services in the catalogue."""
    
    def __init__(self):
        self.catalogue = ServiceCatalogue()
        
    def assess_service(self, service_id: str) -> Dict:
        """
        Assesses a specific service for quality.
        
        Args:
            service_id: ID of the service to assess.
            
        Returns:
            Assessment results including pass/fail status and issues found.
            
        Raises:
            ValueError: If service not found in catalogue.
        """
        services = self.catalogue.services
        matching_services = [s for s in services if s['id'] == service_id]
        
        if not matching_services:
            raise ValueError(f"Service with id {service_id} not found.")
            
        assessment = self._perform_assessment(matching_services[0])
        return assessment

    def _perform_assessment(self, service: Dict) -> Dict:
        """
        Performs quality checks on a service.
        
        Returns:
            Dictionary with overall status and list of issues.