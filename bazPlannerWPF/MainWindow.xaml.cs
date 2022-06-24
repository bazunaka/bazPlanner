using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using static bazPlannerWPF.sqlite_connect;
using static bazPlannerWPF.auth;

namespace bazPlannerWPF
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DateTime now = DateTime.Now;
            Now_time.Content = now.ToString("D");
        }

        private void Connect_to_DB(object sender, RoutedEventArgs e)
        {
           if(sqlite_connect.Connect("test.db"))
            {
                Console.WriteLine("Connected!");
            }

           if(true) //при отсутствии пользователей в БД
            {

            }

            auth a = new auth(); //изменить потом название
            a.Show();

        }

        private void Create_project(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("Created!");
        }
    }
}
