//
//  ContentView.swift
//  WAvE_haptics_watch Watch App
//
//  Created by Rohit Mekkoth on 4/13/24.
//

import SwiftUI
import WatchKit

struct ContentView: View {
    @State private var showAlert = false

    var body: some View {
        VStack {
            Spacer()

            // Logo from your asset catalog
            Image("WAvE")
                .resizable()
                .scaledToFit()
                .frame(width: 50, height: 50)
                .clipShape(Circle()) // Clips the image to a circle
                .overlay(Circle().stroke(Color.blue, lineWidth: 2)) // Optional: Adds a blue stroke outline

            Text("Looks like you're")
                .font(.headline)
                .foregroundColor(Color.blue)

            Text("fatigued!")
                .font(.headline)
                .foregroundColor(Color.blue)

            Spacer()
            Spacer()

            // Dismiss button as seen in your screenshot
            Button(action: {
                self.showAlert = true
                            }) {
                Text("Dismiss")
                    .foregroundColor(.white)
                    .padding()
                    .background(Capsule().fill(Color.blue))
            }
            
            Spacer()
        }
        .onAppear {
            // Play Haptic on Appear
            WKInterfaceDevice.current().play(.notification)
            WKInterfaceDevice.current().play( .underwaterDepthCriticalPrompt)
        }
        
        .alert(isPresented: $showAlert) {
            Alert(title: Text("Please refer to your EFB for further instructions"),
                  dismissButton: .default(Text("OK")))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
func playHaptic() {
        // Choose the type of haptic to play
    WKInterfaceDevice.current().play(.notification)
    }
