"""
Classes from the 'CoreUtils' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


TUTestState = _Class("TUTestState")
NXClient = _Class("NXClient")
CUXPCAgentConnection = _Class("CUXPCAgentConnection")
CUXPCAgent = _Class("CUXPCAgent")
CUXMLRPCClient = _Class("CUXMLRPCClient")
CUWiFiDevice = _Class("CUWiFiDevice")
CUWiFiScanner = _Class("CUWiFiScanner")
CUWiFiTrafficPeer = _Class("CUWiFiTrafficPeer")
CUWiFiManager = _Class("CUWiFiManager")
CUWACSession = _Class("CUWACSession")
CUVoiceSession = _Class("CUVoiceSession")
CUVoiceRequest = _Class("CUVoiceRequest")
CUUserNotificationSession = _Class("CUUserNotificationSession")
CUUserNotificationCustomAction = _Class("CUUserNotificationCustomAction")
CUTDSSession = _Class("CUTDSSession")
CUTDSSeeker = _Class("CUTDSSeeker")
CUTDSProvider = _Class("CUTDSProvider")
CUTDSEndpoint = _Class("CUTDSEndpoint")
CUTDSDevice = _Class("CUTDSDevice")
CUTDSAgent = _Class("CUTDSAgent")
CUTDSXPCConnection = _Class("CUTDSXPCConnection")
CUTDSDaemon = _Class("CUTDSDaemon")
CUTCPServer = _Class("CUTCPServer")
CUTCPConnection = _Class("CUTCPConnection")
CUSystemMonitor = _Class("CUSystemMonitor")
CUSystemMonitorImp = _Class("CUSystemMonitorImp")
CUStateMachine = _Class("CUStateMachine")
CUStateEvent = _Class("CUStateEvent")
CUState = _Class("CUState")
CUSleepWakeMonitor = _Class("CUSleepWakeMonitor")
CUSetupHandler = _Class("CUSetupHandler")
CUSetupStep = _Class("CUSetupStep")
CUSetupStepPreflightWiFi = _Class("CUSetupStepPreflightWiFi")
CUSetupFlow = _Class("CUSetupFlow")
CUServer = _Class("CUServer")
CURunLoopThread = _Class("CURunLoopThread")
CURetrier = _Class("CURetrier")
CUReachabilityMonitor = _Class("CUReachabilityMonitor")
CURPIdentity = _Class("CURPIdentity")
CURangingSample = _Class("CURangingSample")
CURangingPeer = _Class("CURangingPeer")
CURangingMeasurement = _Class("CURangingMeasurement")
CURangingSession = _Class("CURangingSession")
CUPowerSourceLEDInfo = _Class("CUPowerSourceLEDInfo")
CUPowerSource = _Class("CUPowerSource")
CUPowerSourceMonitor = _Class("CUPowerSourceMonitor")
CUPersistentTimer = _Class("CUPersistentTimer")
CUPairingStream = _Class("CUPairingStream")
CUPairingSession = _Class("CUPairingSession")
CUPairedPeer = _Class("CUPairedPeer")
CUPairingIdentity = _Class("CUPairingIdentity")
CUPairingManager = _Class("CUPairingManager")
CUPairingXPCConnection = _Class("CUPairingXPCConnection")
CUPairingDaemon = _Class("CUPairingDaemon")
CUOSRecoveryTarget = _Class("CUOSRecoveryTarget")
CUOSRecoveryProgressEvent = _Class("CUOSRecoveryProgressEvent")
CUNFCDevice = _Class("CUNFCDevice")
CUNFCScanner = _Class("CUNFCScanner")
CUNFCAdvertiser = _Class("CUNFCAdvertiser")
CUNetServiceEndpoint = _Class("CUNetServiceEndpoint")
CUNetServiceDiscovery = _Class("CUNetServiceDiscovery")
CUNetServiceAdvertiser = _Class("CUNetServiceAdvertiser")
CUNetLinkEndpoint = _Class("CUNetLinkEndpoint")
CUNetLinkManager = _Class("CUNetLinkManager")
CUNetInterfaceMonitor = _Class("CUNetInterfaceMonitor")
CUNANEndpoint = _Class("CUNANEndpoint")
CUNANSubscriber = _Class("CUNANSubscriber")
CUNANPublisher = _Class("CUNANPublisher")
CUNANDataSession = _Class("CUNANDataSession")
CUMobileDeviceSession = _Class("CUMobileDeviceSession")
CUMobileDevice = _Class("CUMobileDevice")
CUMobileDeviceDiscovery = _Class("CUMobileDeviceDiscovery")
CUMobileDeviceMonitorContext = _Class("CUMobileDeviceMonitorContext")
CUMFiSession = _Class("CUMFiSession")
CUMFiWriteRequest = _Class("CUMFiWriteRequest")
CUMFiReadRequest = _Class("CUMFiReadRequest")
CUMFiDeviceDiscovery = _Class("CUMFiDeviceDiscovery")
CUMessageSessionXPCConnection = _Class("CUMessageSessionXPCConnection")
CUMessageSessionServer = _Class("CUMessageSessionServer")
CUMessageSession = _Class("CUMessageSession")
CUMessageRequestEntry = _Class("CUMessageRequestEntry")
CULogHandle = _Class("CULogHandle")
CULiveAudioPeerSession = _Class("CULiveAudioPeerSession")
CULiveAudioSession = _Class("CULiveAudioSession")
CULiveAudioServerSession = _Class("CULiveAudioServerSession")
CULiveAudioServer = _Class("CULiveAudioServer")
CULiveActionPeerSession = _Class("CULiveActionPeerSession")
CULiveAction = _Class("CULiveAction")
CUKeyValueStoreWriter = _Class("CUKeyValueStoreWriter")
CUKeyValueStoreReader = _Class("CUKeyValueStoreReader")
CUKeychainItem = _Class("CUKeychainItem")
CUKeychainManager = _Class("CUKeychainManager")
CUWriteRequest = _Class("CUWriteRequest")
CUReadRequest = _Class("CUReadRequest")
CUIDSSession = _Class("CUIDSSession")
CUIDSWriteRequest = _Class("CUIDSWriteRequest")
CUIDSReadRequest = _Class("CUIDSReadRequest")
CUHomeKitManager = _Class("CUHomeKitManager")
CUHomeKitFindPairedPeerContext = _Class("CUHomeKitFindPairedPeerContext")
CUHomeKitResolvableAccessory = _Class("CUHomeKitResolvableAccessory")
CUFileResponse = _Class("CUFileResponse")
CUFileQuery = _Class("CUFileQuery")
CUFileItem = _Class("CUFileItem")
CUFileServer = _Class("CUFileServer")
CUFileServerSession = _Class("CUFileServerSession")
CUFileClient = _Class("CUFileClient")
CUEnvironment = _Class("CUEnvironment")
CUEndpoint = _Class("CUEndpoint")
CUDashboardServer = _Class("CUDashboardServer")
CUDashboardClient = _Class("CUDashboardClient")
CUConnection = _Class("CUConnection")
CUCoalescer = _Class("CUCoalescer")
CUBonjourDevice = _Class("CUBonjourDevice")
CUBonjourBrowser = _Class("CUBonjourBrowser")
CUBonjourAdvertiser = _Class("CUBonjourAdvertiser")
CUBluetoothScalablePipe = _Class("CUBluetoothScalablePipe")
CUBluetoothUpdateAccessoryDevicesRequest = _Class(
    "CUBluetoothUpdateAccessoryDevicesRequest"
)
CUBluetoothRelayMessage = _Class("CUBluetoothRelayMessage")
CUBluetoothDevice = _Class("CUBluetoothDevice")
CUBluetoothClient = _Class("CUBluetoothClient")
CUBluetoothFindDeviceRequest = _Class("CUBluetoothFindDeviceRequest")
CUBluetoothClassicConnection = _Class("CUBluetoothClassicConnection")
CUBLEServer = _Class("CUBLEServer")
CUBLEDevice = _Class("CUBLEDevice")
CUBLEScanner = _Class("CUBLEScanner")
CUBLEConnection = _Class("CUBLEConnection")
CUBLEAdvertiser = _Class("CUBLEAdvertiser")
CUBitCoder = _Class("CUBitCoder")
CUBitCoderEncryptRequest = _Class("CUBitCoderEncryptRequest")
CUBitCoderDecryptResponse = _Class("CUBitCoderDecryptResponse")
CUBitCoderDecryptRequest = _Class("CUBitCoderDecryptRequest")
CUAudioPlayer = _Class("CUAudioPlayer")
CUAudioRequest = _Class("CUAudioRequest")
CUAppleIDClient = _Class("CUAppleIDClient")
CAAnimationDelegateBlockHelper = _Class("CAAnimationDelegateBlockHelper")
CoreUtilsNSSubrangeData = _Class("CoreUtilsNSSubrangeData")
