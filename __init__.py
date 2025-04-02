import unrealsdk
from Mods import ModMenu

class PrecisionMouseControl(ModMenu.SDKMod):
    Name = "Precision Mouse Control"
    Description = "Allows you to set the mouse sensitivity in smaller increments - Credits: Based on the original BLCM mod 'Uncapped Pause Menu Settings' by OB4MA."
    Author = "Swift Delivery"
    Version = "1.2"
    SaveEnabledState = ModMenu.EnabledSaveType.LoadWithSettings

    def Enable(self):
        self.SetMouseSensitivityIncrement()
        unrealsdk.Log(f"[{self.Name}] Mod Enabled")

    def Disable(self):
        unrealsdk.Log(f"[{self.Name}] Mod Disabled")

    def SetMouseSensitivityIncrement(self):
        # Find the WillowProfileSettings object.
        wps = unrealsdk.FindObject("WillowProfileSettings", "Transient.WillowProfileSettings_0")
        if not wps:
            unrealsdk.Log(f"[{self.Name}]: Could not find WillowProfileSettings_0.")
            return

        # Loop through the ProfileMappings to locate the one for MouseSensitivity.
        for mapping in wps.ProfileMappings:
            if mapping.Name == "MouseSensitivity":
                mapping.MinVal = 1
                mapping.MaxVal = 100
                mapping.RangeIncrement = 1
                break

# Register the mod so that it appears in the mod menu.
ModMenu.RegisterMod(PrecisionMouseControl())
