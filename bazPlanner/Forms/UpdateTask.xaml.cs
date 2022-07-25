using System.Diagnostics;
using System.Windows;
using bazPlanner.Models;

namespace bazPlanner.Forms
{
    public partial class UpdateTask : Window
    {
        //Add new task.
        public UpdateTask()
        {
            InitializeComponent();
        }

        private void UpdateThisTask(object sender, RoutedEventArgs e)
        {
            //Not work!
            int selectedItem = (int)((MainWindow)Application.Current.MainWindow).dataGrid.SelectedItems[0];
            Debug.WriteLine(selectedItem.ToString());
            //Database.UpdateTask();
        }
    }
}
